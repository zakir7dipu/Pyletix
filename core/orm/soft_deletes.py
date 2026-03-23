class SoftDeletes:
    def delete(self):
        if hasattr(self, "deleted_at"):
            import datetime
            self.deleted_at = datetime.datetime.now().isoformat()
            self.save()
            return True
        return super().delete()

    @classmethod
    def query(cls):
        builder = super().query()
        # Automatically exclude soft deleted records unless explicitly requested
        builder.where("deleted_at", None, "IS")
        return builder

    def restore(self):
        self.deleted_at = None
        self.save()

    def force_delete(self):
        return super().delete()
