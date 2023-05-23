<?php
include 'session.php';
?>
<link rel="import" href="header.html">
<div class="container">
	<div class="page-header">
    	<h1 class="h2">&nbsp; 메인페이지</h1>
    </div>
<div class="row">
    <center>
    <?php
    echo "로그인 성공";
    echo "id 는 ".$_SESSION['id']."입니다.\n";
    ?>
    </center>
<center>
<nav class="navbar navbar-default navbar-static-top">
    <div class="container-fluid">
        <div class="navbar-header">
            <?php if (isset($_SESSION['user_id'])) { ?>
                <li><a href="">환영합니다 <?php echo $_SESSION['user_id']; ?>님</a></li>
                <li><a href="logout.php">Log Out</a></li>
            <?php } else { ?>

             <?php } ?>
			</ul>
        </div>
    </div>
</center>
</body>
</html>
<br>
<br>
<br>
<html>
    <body>
<link rel="stylesheet" href="style.css">     
<br>  </br>
<button id="btn1" onClick="location.href='logout.php'"> 로그아웃 </button>        
</body>
</html>
