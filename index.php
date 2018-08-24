<?php

$username = "";
$password = "";
$unameErr = $pwErr = "";
$unameDB = $pwDB = 0;
   
   if($_SERVER["REQUEST_METHOD"] == "POST") {
	   	if (empty($_POST["uname"])) {
	    $unameErr = "User name is required";
	    $unameDB = 0;
	  } else {
	    $username = test_input($_POST["uname"]);
	    $unameDB = 1;
	  }
	  
	  if (empty($_POST["pw"])) {
	    $pwErr = "Password is required";
	    $pwDB = 0;
	  } else {
	    $password = test_input($_POST["pw"]);
	    $pwDB = 1;
	  }

	   	$servername = 'localhost';
		$DBusername = 'root';
		$DBpassword = '';
		$dbname = "electric";

		// Create connection
		$conn = new mysqli($servername, $DBusername, $DBpassword, $dbname);
		// Check connection
		if ($conn->connect_error) {
		    die("Connection failed: " . $conn->connect_error);
		} 
      // username and password sent from form 
      
      if(($unameDB==1) && ($pwDB==1))
      {
      	
		$sql = "SELECT * FROM `user` WHERE `username` LIKE '$username'";
		$result = $conn->query($sql);

		if ($result->num_rows > 0) {
		    // output data of each row
		    while($row = $result->fetch_assoc()) {

		    	if(($row["username"] == $username) && ($row["password"] == $password) ){
		    		session_start();
		    		$_SESSION['login_user'] = $username;

		    		header('Refresh: 0.1; URL = usage.php');
		    	}
				else{
		    		echo "Invalid password";
		    	}
		        
		    }
		} 
		else {
		    echo "Invalid username.";
		}
		$conn->close();

      }
      
   }

   function test_input($data) {
	  $data = trim($data);
	  $data = stripslashes($data);
	  $data = htmlspecialchars($data);
	  return $data;
	}
?>



<html>
<head>
	<title> ECSU Electric Company </title>
</head>

<body>
	<h2>Welcome to ECSU Electric Company. The Number 1. Electric Company </h2>

	<form action="" method="post">
		
		<table>
			<h3> Login</h3>
			<tr>
				<td>
					<label> User Name: </label>
				</td>
				<td>
					<input type="text" name="uname">
				</td>
			</tr>
			<tr>
				<td>
					<label> Password: </label>
				</td>
				<td>
					<input type="Password" name="pw">
				</td>
			</tr>
			<tr>
				<td>
					<input type="submit" name="submit" value="Login">
				</td>
				<td>
					<a href="signup.php">Sign Up</a>
				</td>
			</tr>
		</table>
	</form>
</body>
</html>