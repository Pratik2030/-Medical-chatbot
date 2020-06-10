<?php header('Content-Type:charset=utf-8');
$hostname_localhost ="localhost";
$database_localhost ="chatbot";
$username_localhost ="root";
$password_localhost ="root";
$localhost = mysql_connect($hostname_localhost,$username_localhost,$password_localhost)
or
trigger_error(mysql_error(),E_USER_ERROR);
mysql_select_db($database_localhost, $localhost);
$day1 =$_REQUEST['day'];
$time11 =$_REQUEST['time1'];
$time12 =$_REQUEST['time2'];

$query_search = "INSERT INTO chatbot.schedule(SL_NO, day, time1, time2) VALUES(null,'$day1','$time11','$time12')";
$query_exec = mysql_query($query_search) or die(mysql_error());
$rows = mysql_num_rows($query_exec);
if($rows == 0) { 
 echo "0"; 
 
 }
 else  {
	echo "1"; 
}


 



?>












