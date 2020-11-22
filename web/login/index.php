<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/bootstrap.css">
    <script src="https://www.google.com/recaptcha/api.js"></script>

    <title>Login Form in PHP with Sessions</title>
    
</head>
<body style="background:#CCC;">
    <div class="container">
        <div class="row">
            <div class="col-lg-6 m-auto">
                <div class="card bg-dark mt-5">
                    <div calss="card-title bg-primary text-white mt-5">
                        <h3 style="color:white;" class="text-center py-3">Login</h3>
                    </div>


                    <?php 
                        if(@$_GET['Empty']==true)
                        {
                    ?>
                        <div class="alert-light text-danger text-center py-3"><?php echo $_GET['Empty'] ?></div>                                
                    <?php
                        }
                    ?>


                    <?php 
                        if(@$_GET['Invalid']==true)
                        {
                    ?>
                        <div class="alert-light text-danger text-center py-3"><?php echo $_GET['Invalid'] ?></div>                                
                    <?php
                        }

                    ?>


                    <div class="card-body">

                        <form action="process.php" method="POST">
                            <input type="text" name="UName" placeholder=" User Name" class="form-control mb-3" value="<?php if(isset($_COOKIE["member_login"])){ echo $_COOKIE["member_login"]; }?>">
                            <input type="password" name="Password" placeholder=" Password" class="form-control mb-3"  value="<?php if(isset($_COOKIE["member_password"])){ echo $_COOKIE["member_password"]; }?>">
                            <div class="form-group">
                            <input type="checkbox" name="remember" <?php if(isset($_COOKIE["member_login"])){ ?>checked<?php } ?>/>
                                <label style="color:white;">Remember me</label>
                            </div>
                            <div class="g-recaptcha" data-sitekey="site-key"></div>
                            
                            <button class="btn btn-success mt-2" name="Login">Login</button>
                            
                            <a class="mb-9 text-right" style="float:right; margin-top:10px;" href="register.php"name="signUp">Create Account</a>

                            
                        </form>


                    </div>
                </div>
            </div>
        </div>
    </div>
</body>
</html>