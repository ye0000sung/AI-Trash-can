<html>
<head>
  <meta http-equiv="Content-Type" content="text/html; 
    charset=UTF-8" />
<title>메인페이지</title>
<link rel="stylesheet" href="style.css">


</head>

<body>
    
<nav class="navbar navbar-default navbar-static-top">
    <div class="container-fluid">
        <div class="navbar-header">
        <button id="btn2" onClick="location.href='lunch_check.html'"> 로그인 </button>      
            <?php if (isset($_SESSION['user_id'])) { ?>
                <li><a href="">환영합니다 <?php echo $_SESSION['user_id']; ?>님</a></li>
                <li><a href="logout.php">Log Out</a></li>
            <?php } else { ?>
             <?php } ?>
			</ul>
        </div>
    </div>
</nav>
