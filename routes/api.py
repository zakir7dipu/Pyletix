def register(router):
    router.prefix("/api/v1")
    router.get("/users", "UserResourceController@index")
    router.get("/users/:id", "UserResourceController@show")
    router.prefix("") # Reset prefix
