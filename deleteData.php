<?php

    //使用者資訊
    $host = "localhost";
    $user = "nina";
    $pass = "1234";

    //資料庫資訊
    $databaseName = "iot";
    $tableName = "light";


    //連結資料庫
    $con = mysqli_connect($host,$user,$pass, $databaseName);
    //$dbs = mysql_select_db($databaseName, $con);


    //資料庫Sql query語法
    $sql = "TRUNCATE TABLE $tableName";    //殺掉資料庫
 

    //執行query語法
   // $result = mysqli_query($con,$sql);
    mysqli_query($con,$sql);
   
   mysqli_close($con);//關閉資料庫
   header('Location: http://localhost/IOT3/home.html');  //回到主畫面
?>
