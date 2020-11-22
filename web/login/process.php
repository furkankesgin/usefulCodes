<?php
require_once('connection.php');
session_start();
    if(isset($_POST['Login']))
    {
        $secretKey= "secret-key";
        $responseKey = $_POST['g-recaptcha-response'];
        $userIP = $_SERVER['REMOTE_ADDR'];
        $url = "https://www.google.com/recaptcha/api/siteverify?secret=$secretKey&response=$responseKey&remoteip=$userIP";
        $response = file_get_contents($url);
        $response = json_decode($response);
        $username = $_POST["UName"];
        $password = $_POST["Password"];
        $password = md5($password);

        if(empty($_POST['UName']) || empty($_POST['Password']))
        {
            header("location:index.php?Empty=Please fill in the blanks");
        }
            else
                {

                    
                    if($response->success){
                        if(!empty($_POST["remember"]))
                        {
                            setcookie("member_login", $_POST["UName"],time()+ (10 * 365 * 24 * 60 *60));
                            setcookie("member_password", $_POST["Password"],time()+ (10 * 365 * 24 * 60 *60));

                        }
                        else
                        {
                            if(isset($_COOKIE["member_login"]))
                            {
                                setcookie("member_login","");
                                setcookie("member_password","");

                            }
                        }

                        $query="select * from users where uName='".$_POST['UName']."' and uPass='".$password."'";
                        $result = mysqli_query($con,$query);
                
                        if(mysqli_fetch_assoc($result))
                        {
                            $_SESSION['LAST_ACTIVITY'] = time();
                            $_SESSION['User'] = $_POST['UName'];
                            header("location:welcome.php");
                        }
                            else
                            {
                                header("location:index.php?Invalid= Please enter correct username and password ");
                            }
                    }
                    else
                    {
                        header("location:index.php?Invalid= verify humanity ");
                    }
                    
                }
        
    }







    




    //REGISTER
    else if(isset($_POST['Register']))
    {
        if(empty($_POST['UName']) || empty($_POST['Password']))
        {
            header("location:register.php?Empty=Please fill in the blanks");
        }
        else
        {
            $username = $_POST["UName"];
            $password = $_POST["Password"];

            $passHash = md5($password);  //32 karakterlik veritabaninda alan acilmali!!!

            $sql_u = "SELECT * FROM users WHERE uName='$username'";
            $res_u = mysqli_query($con, $sql_u);

            if (mysqli_num_rows($res_u) > 0) {
            $name_error = "Sorry... username already taken"; 	
            header("location:register.php?Invalid= Sorry... username already taken");
            }
            else{
            $query = "INSERT INTO users(uName, uPass) VALUES('$username','$passHash')";
            $result = mysqli_query($con,$query);
            if(!mysqli_fetch_assoc($result))
            {
                header("location:index.php");
            }
            else
            {
                header("location:register.php?Invalid=$result");
            }
            }
        
    }
    }

?>