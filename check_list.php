<?php header('Content-Type:charset=utf-8');
$hostname_localhost ="localhost";
$database_localhost ="chatbot";
$username_localhost ="root";
$password_localhost ="root";
$localhost = mysql_connect($hostname_localhost,$username_localhost,$password_localhost)
or
trigger_error(mysql_error(),E_USER_ERROR);

mysql_select_db($database_localhost, $localhost);
$date7 = date("Y-m-d");
$query_search = "select * from chatbot.appointmentdb where date = '".$date7."'";
$result1 = mysql_query($query_search);
		$json["data"]= array();
		
		if(mysql_num_rows($result1))
		{
			$json["data"]= array();
		    while($row=mysql_fetch_assoc($result1))
			{
		       $product = array();
				$product["fname"] = $row["fname"];
				$product["lname"] = $row["lname"];
				$product["date"] = $row["date"];
				$product["sno"] = $row["sno"];
				$product["location"] = $row["location"];
				$product["dtype"] = $row["dtype"];
									
                array_push($json["data"], $product);
			}
		}
		
		echo json_encode($json);
?>














