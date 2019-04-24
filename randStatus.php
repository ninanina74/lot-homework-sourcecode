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


 for ($i=0;$i<30;$i++)
   {      //i數值少於40就創建資料
    $sql = "UPDATE $tableName SET STATUS=RAND()";
    
    //執行query語法
    mysqli_query($con,$sql);

    }

   
  mysqli_close($con);  //關閉資料庫
  header('Location: http://localhost/IOT3/home.html'); //回主畫面
?>
