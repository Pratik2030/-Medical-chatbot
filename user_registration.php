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
$mname1=$_REQUEST['mname'];
$lname1=$_REQUEST['lname'];
$contact1 =$_REQUEST['contact'];
$loc1=$_REQUEST['loc'];
$email1=$_REQUEST['email'];
$gender1=$_REQUEST['gender'];
$uname1=$_REQUEST['uname'];
$pwd1=$_REQUEST['pwd'];

$query_search = "INSERT INTO chatbot.user(fname,mname,lname,contact,email,gender,uname,pwd,location) VALUES('$fname1','$mname1','$lname1','$contact1','$email1','$gender1','$uname1','$pwd1','$loc1')";
$query_exec = mysql_query($query_search) or die(mysql_error());
$rows = mysql_num_rows($query_exec);

 if($rows == 0) { 
 echo "0"; 
 }
 else  {
	echo "1"; 
}
