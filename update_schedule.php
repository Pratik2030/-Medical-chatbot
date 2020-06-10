<?php header('Content-Type:charset=utf-8');
$hostname_localhost ="localhost";
$database_localhost ="chatbot";
$username_localhost ="root";
$password_localhost ="root";
$localhost = mysql_connect($hostname_localhost,$username_localhost,$password_localhost)
or
trigger_error(mysql_error(),E_USER_ERROR);

mysql_select_db($database_localhost, $localhost);

$day5 =$_REQUEST['day'];
$time5=$_REQUEST['time1'];
$time6=$_REQUEST['time2'];

$query_search = "select * from schedule where day = '".$day5."'";
$result1 = mysql_query($query_search);


$query_search = "UPDATE schedule SET time1 ='".$time5."', time2='".$time6."' WHERE day = '".$day5."'";
$query_exec = mysql_query($query_search) or die(mysql_error());
$rows = mysql_num_rows($query_exec);
if($rows == 0) { 
echo "0"; 
 
}
else  {
echo "1"; 
}






?>














