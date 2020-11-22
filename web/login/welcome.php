<?php
    $TimeToExpired = 60;
    session_start();
    if(isset($_SESSION['User']))
    {
        echo 'Welcome '. $_SESSION['User'].'<br/>';
        echo '<a href="logout.php?logout">Logout</a>';
 
    }
    else
    {
        header("location:index.php");
    }
    if (isset($_SESSION['LAST_ACTIVITY']) && (time() - $_SESSION['LAST_ACTIVITY'] > $TimeToExpired)) {
        session_unset();    
        session_destroy();   
        ?>
        <script>alert("session expired");</script>
        <?php
        header("location:index.php");
    }
    // update last activity time stamp
?>