<?php
session_start();
if(!isset($_SESSION['id'])) //세션이 존재하지 않을 때
{    header ('Location: ./index.html');
}
$id=$_POST['id'];

$hostname = 'localhost';
$username = 'yesungyun1'; //아이디
$password = 'ys01290129@';
$dbname = 'xxpodo'; //데이터베이스 이름
$conn = mysqli_connect($hostname, $username, $password, $dbname);

 ?>

