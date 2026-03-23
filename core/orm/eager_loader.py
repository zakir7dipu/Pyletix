class EagerLoader:
    @staticmethod
    def load(models, relations):
        if not models:
            return models

        for relation_name in relations:
            # Assume for now relation_name corresponds to a method on the model
            first_model = models[0]
            if not hasattr(first_model, relation_name):
                continue
            
            # Get relation object from the first model instance
            relation_obj = getattr(first_model, relation_name)()
            
            # Fetch and attach
            EagerLoader._fetch_and_attach(models, relation_name, relation_obj)
        
        return models

    @staticmethod
    def _fetch_and_attach(models, relation_name, relation_obj):
        from .relationships import HasOne, HasMany, BelongsTo
        
        if isinstance(relation_obj, (HasOne, HasMany)):
            foreign_key = relation_obj.foreign_key
            local_key = relation_obj.local_key
            ids = [getattr(m, local_key) for m in models]
            
            # Fetch all related models in one query
            # builder = relation_obj.related_model.query().whereIn(foreign_key, ids)
            # Since I don't have whereIn yet, I'll use a hack or implement whereIn
            related_models = relation_obj.related_model.query().where(foreign_key, ids, "IN").get()
            
            # Map them
            from collections import defaultdict
            mapping = defaultdict(list)
            for rm in related_models:
                # related_models are Row objects or Model objects?
                # BaseModel.all() returns Model objects. QueryBuilder.get() returns Row objects.
                # I should make QueryBuilder aware of the Model class to return objects.
                val = getattr(rm, foreign_key)
                mapping[val].append(rm)
            
            for m in models:
                val = getattr(m, local_key)
                if isinstance(relation_obj, HasOne):
                    setattr(m, f"_{relation_name}_cache", mapping[val][0] if mapping[val] else None)
                else:
                    setattr(m, f"_{relation_name}_cache", mapping[val])
        
        elif isinstance(relation_obj, BelongsTo):
            foreign_key = relation_obj.foreign_key
            owner_key = relation_obj.owner_key
            ids = [getattr(m, foreign_key) for m in models if getattr(m, foreign_key)]
            
            related_models = relation_obj.related_model.query().where(owner_key, ids, "IN").get()
            
            mapping = {getattr(rm, owner_key): rm for rm in related_models}
            
            for m in models:
                val = getattr(m, foreign_key)
                setattr(m, f"_{relation_name}_cache", mapping.get(val))
