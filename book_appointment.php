<?php header('Content-Type:charset=utf-8');
$hostname_localhost ="localhost";
$database_localhost ="chatbot";
$username_localhost ="root";
$password_localhost ="root";
$localhost = mysql_connect($hostname_localhost,$username_localhost,$password_localhost)
or
trigger_error(mysql_error(),E_USER_ERROR);
mysql_select_db($database_localhost, $localhost);
$fname1 =$_REQUEST['fname'];
$lname1=$_REQUEST['lname'];
$contact1 =$_REQUEST['contact'];
$gender1=$_REQUEST['gender'];
$type1=$_REQUEST['type'];
$loc1=$_REQUEST['loc'];
$date7 = date("Y-m-d");
//NOW()

$query_search = "INSERT INTO chatbot.appointmentdb(sno,fname,lname,contact,location,gender,dtype,date) VALUES(null,'$fname1','$lname1','$contact1','$loc1','$gender1','$type1','$date7')";
$query_exec = mysql_query($query_search) or die(mysql_error());
$rows = mysql_num_rows($query_exec);
if($rows == 0) { 
 echo "0"; 
 
 }
 else  {
	echo "1"; 
}


 



?>












