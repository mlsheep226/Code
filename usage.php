<!DOCTYPE HTML> 
<html>
<head>
</head>
<body> 

<h1>Usage Report</h1>
<?php
session_start();
$servername = 'localhost';
$DBusername = 'root';
$DBpassword = '';
$dbname = 'electric';
$units = 0;

// Create connection
$conn = new mysqli($servername, $DBusername, $DBpassword, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}
$username = $_SESSION['login_user']; 
$sql = "SELECT * FROM `usage` WHERE `username` LIKE '$username'";
$sql2 = "SELECT `firstname`, `lastname` FROM `user` WHERE `username` LIKE '$username'";
$result = $conn->query($sql2);
if ($row2 = $result->fetch_assoc()) {
	echo "<h3>Welcome ".$row2["firstname"]."!</h3>";
	echo "<table border = '1px' width = 100%>";
	echo "<bold><tr><td>Name</td><td>Username</td><td>Month</td><td>Year</td><td>Units Used</td></tr><bold>";
	echo "<tr><td>".$row2["firstname"]." ".$row2["lastname"]."</td>";
	$result = $conn->query($sql);
	while($row = $result->fetch_assoc()) {
		$units = $row["units"];
		$month = $row["month"];
		echo "<td>".$row["username"]."</td><td>". $row["month"]."</td><td>".$row["year"]."</td><td>".$row["units"]."</td></tr>";
	}
}
echo "</table>";
echo " ";
$amount_due = $units*1.56;
echo " ";
echo "Amount Due on Bill is: $".$amount_due." for ".$units." Watt/Hours for the Month of ".$month;
$conn->close();

?>
<br>
<a href="logout.php"><button>Logout</button></a>

</body>
</html>