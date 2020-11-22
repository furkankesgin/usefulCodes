<!DOCTYPE html>
<html>
<head>
    <meta charset='utf-8'>
    <meta http-equiv='X-UA-Compatible' content='IE=edge'>
    <title>Page Title</title>
    <meta name='viewport' content='width=device-width, initial-scale=1'>
    <link rel="stylesheet" href="css/bootstrap.css">
    <script src="https://www.google.com/recaptcha/api.js"></script>
</head>
<body>
    <body style="background:#CCC;">
        <div class="container">
            <div class="row">
                <div class="col-lg-6 m-auto">
                    <div class="card bg-dark mt-5">
                        <div calss="card-title bg-primary text-white mt-5">
                            <h3 style="color:white;" class="text-center py-3">Register</h3>
                        </div>
    
                        <?php 

                       
                        $ip = $_SERVER['REMOTE_ADDR'] . "\t" .date("M,d,Y h:i:s A");

                        $myfile = fopen("registerIPs.txt", "a+") or die("Unable to open file!");
                        $txt = "$ip\n";
                        fwrite($myfile, $txt);
                        fclose($myfile);

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
                                <input type="text" name="UName" placeholder=" User Name" class="form-control mb-3">
                                <input type="password" name="Password" placeholder=" Password" class="form-control mb-3">
                                <div class="g-recaptcha" data-sitekey="6LcufecZAAAAALbCdcMYMx8_QviX-A48I-PQim4K"></div>
    
                                <button class="btn btn-success mt-3" name="Register">Register</button>
                                <a class="mb-9 text-right" style="float:right; margin-top:10px;" href="index.php"name="signUp">Already have account?</a>

    
                            </form>
    
    
                        </div>
                    </div>
                </div>
            </div>
        </div>
</body>
</html>