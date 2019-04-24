<?php
 //使用者資訊
    $host = "localhost";
    $user = "nina";
    $pass = "1234";

    //資料庫資訊
    $databaseName = "iot";
    $tableName = "light";

$_news=array();
exec("python myEA.py",$_news);
var_dump($_news);

header('Location: http://localhost/IOT3/home.html');
?>