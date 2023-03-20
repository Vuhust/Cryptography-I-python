<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">
   
  <title>VTIST - Login</title>
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="vendor/bootstrap/css/bootstrap.min.css" rel="stylesheet" type="text/css">
  <link href="css/ruang-admin.min.css" rel="stylesheet">

</head>

<body class="bg-gradient-login">
  <!-- Login Content -->
  <div class="container-login">
    <div class="row justify-content-center">
      <div class="col-xl-6 col-lg-12 col-md-9">
        <div class="text-center" style="margin-top: 60px;">
          <h1 class="h4 text-gray-900" style="font-size: 40px;">Login</h1>
        </div>
        <div class="card shadow-sm my-3">
          <div class="card-body p-0">
            <div class="row">
              <div class="col-lg-12">
                <div class="login-form">
                  <form class="user">
                    <div class="form-group" style="display: flex;">
                      <input type="email" class="form-control" id="exampleInputEmail" aria-describedby="emailHelp"
                        placeholder="User" style="z-index: 1; background-color: transparent;">
                        <i class="fas fa-user-alt" style="margin-left: -25px; margin-top: 12px;"></i>
                      </div>
                    <div class="form-group" style="display: flex;">
                      <input type="password" class="form-control" id="exampleInputPassword" placeholder="Password" style="z-index: 1; background-color: transparent;">
                      <i class="fas fa-lock" style="margin-left: -25px; margin-top: 12px;"></i>
                    </div>
                    <div class="form-group">
                      <div class="custom-control custom-checkbox small" style="line-height: 1.5rem;">
                        <input type="checkbox" class="custom-control-input" id="customCheck">
                        <label class="custom-control-label" for="customCheck">Remember
                          Me</label>
                      </div>
                    </div>
                    <div class="form-group">
                      <a href="index" class="btn btn-primary btn-block">Login</a>
                    </div>
                    <hr>
                    <a href="index" class="btn btn-google btn-block">
                      <i class="fab fa-google fa-fw"></i> Login with Google
                    </a>
                    <a href="index" class="btn btn-facebook btn-block">
                      <i class="fab fa-facebook-f fa-fw"></i> Login with Facebook
                    </a>
                  </form>
                  <hr>
                  <div style="display: flex; justify-content: space-between;">
                    <div class="text-left">
                      <a class="font-weight-bold small" href="#">I forgot my password</a>
                    </div>
                    <div class="" style="">
                      <a class="font-weight-bold small" href="register">Create an Account!</a>
                    </div>
                  </div>
                  <div class="text-center">
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <!-- Login Content -->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>
  <script src="js/ruang-admin.min.js"></script>
</body>

</html>
