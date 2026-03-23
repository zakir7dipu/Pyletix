def register(router):
    router.get("/login", "AuthController@show_login")
    router.get("/register", "AuthController@show_register")
    router.get("/logout", "AuthController@logout")
    router.get("/users", "UserController@index")
    router.get("/dashboard", "DashboardController@index")
    router.get("/posts", "PostController@index")
    router.get("/posts/create", "PostController@create")
