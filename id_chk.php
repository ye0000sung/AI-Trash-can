<?php
$hostname = 'localhost';
$username = 'yesungyun1'; //아이디
$password = 'ys01290129@';
$dbname = 'xxpodo'; //데이터베이스 이름
$conn = mysqli_connect($hostname, $username, $password, $dbname);

    $id = $_GET['id'];

    if(!$userid){
        echo "
        <p>아이디를 입력해주세요.</p>
        <center><input type=button value=창닫기 onclick='self.close()'></center>
        ";
    } else{
        $sql = $db -> prepare("SELECT * FROM savelunch WHERE id=:id");
        $sql -> bindParam(':id',$id);
        $sql -> execute();
        $count = $sql -> rowCount();

            if($count<1){
                echo "
                <p>사용 가능한 아이디입니다.</p>
                <center><input type=button value=창닫기 onclick='self.close()'></center>
                ";
            } else{
                echo "
                <p>이미 존재하는 아이디입니다.</p>
                <center><input type=button value=창닫기 onclick='self.close()'></center>
                ";
            }
    }
?>
<!DOCTYPE html>
<html lang="kor">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>중복확인</title>
</head>
</html>
