
<?php

$hostname = 'localhost';
$username = 'yesungyun1'; //아이디
$password = 'ys01290129@';
$dbname = 'xxpodo'; //데이터베이스 이름
$conn = mysqli_connect($hostname, $username, $password, $dbname);

$id = $_POST['id'];
$pw = $_POST['pw'];

$check="SELECT * from savelunch WHERE id='$id'";
$result=$conn->query($check);
if($result->num_rows==1){
  echo ("중복된 id입니다");
  exit();
}

$qurry1 = "insert into savelunch values ('".$id."','".$pw."')";
mysqli_query($conn,$qurry1);
	
    echo "<script>alert(\"회원정보 입력성공\");</script>";
  echo("<script>location.replace('index.html');</script>"); 

?>

