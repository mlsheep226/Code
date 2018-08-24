<!DOCTYPE HTML>  
<html>
<head>
<style>
.error {color: #FF0000;}
</style>
</head>
<body>  

<?php
// define variables and set to empty values
$FnameErr = $LnameErr = $UnameErr = $PwordErr = $emailErr = $TelephoneErr = $addressErr = "";
$fname = $lname = $uname = $pword = $email = $telephone = $address = "";
$FnameDB = $LnameDB = $emailDB = $genderDB = $commentDB = $websiteDB = 0;

if ($_SERVER["REQUEST_METHOD"] == "POST") {
  if (empty($_POST["fname"])) {
    $FnameErr = "First Name is required";
    $FnameDB = 0;
  } else {
    $fname = test_input($_POST["fname"]);
    $FnameDB = 1;
  }

  if (empty($_POST["lname"])) {
    $LnameErr = "Last Name is required";
    $LnameDB = 0;
  } else {
    $lname = test_input($_POST["lname"]);
    $LnameDB = 1;
  }
  
  if (empty($_POST["uname"])) {
    $UnameErr = "First Name is required";
    $UnameDB = 0;
  } else {
    $uname = test_input($_POST["uname"]);
    $UnameDB = 1;
  }

  if (empty($_POST["pword"])) {
    $PwordErr = "User Name is required";
    $PwordDB = 0;
  } else {
    $pword = test_input($_POST["pword"]);
    $PwordDB = 1;
  }

  if (empty($_POST["email"])) {
    $emailErr = "Email is required";
    $emailDB = 0;
  } else {
    $email = test_input($_POST["email"]);
    $emailDB = 1;
  }
    
  if (empty($_POST["telephone"])) {
    $telephone = "";
  } else {
    $telephone = test_input($_POST["telephone"]);
  }

  if (empty($_POST["address"])) {
    $address = "";
  } else {
    $address = test_input($_POST["address"]);
  }

}

function test_input($data) {
  $data = trim($data);
  $data = stripslashes($data);
  $data = htmlspecialchars($data);
  return $data;
}
?>

<?php
if(($FnameDB==1) && ($LnameDB==1) && ($UnameDB==1) && ($PwordDB==1) )
{
$servername = 'localhost';
$username = 'root';
$password = '';
$dbname = "electric";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
} 

// insert query
$sql = "INSERT INTO `user` (`firstname`, `lastname`, `username`, `password`, `telephone`, `email`, `address`, `role`) VALUES ('$fname', '$lname', '$uname', '$pword', '$telephone', '$email', '$address', '0');";
if ($conn->query($sql) === TRUE) {
    echo "Your entry has been successfully inserted";
    header('Refresh: 2; URL = index.php');
} else {
    echo "Error entering into the database: " . $conn->error;
}

$conn->close();
}

?>


<h2>Sign up to ECSU Electric.</h2>
<p><span class="error">* required field.</span></p>
<form method="post" action="<?php echo htmlspecialchars($_SERVER["PHP_SELF"]);?>">  
  First Name: <input type="text" name="fname" value="<?php echo $fname;?>">
  <span class="error">* <?php echo $FnameErr;?></span>
  <br><br>

  Last Name: <input type="text" name="lname" value="<?php echo $lname;?>">
  <span class="error">* <?php echo $LnameErr;?></span>
  <br><br>

  User Name: <input type="text" name="uname" value="<?php echo $uname;?>">
  <span class="error">* <?php echo $UnameErr;?></span>
  <br><br>

  Password: <input type="text" name="pword" value="<?php echo $pword;?>">
  <span class="error">* <?php echo $PwordErr;?></span>
  <br><br>

  E-mail: <input type="text" name="email" value="<?php echo $email;?>">
  <span class="error">* <?php echo $emailErr;?></span>
  <br><br>

  Address: <input type="text" name="address" value="<?php echo $address;?>">
  <br><br>

  Telephone: <input type="text" name="telephone" value="<?php echo $telephone;?>">
  <br><br>
  
  <input type="submit" name="submit" value="Submit">  
</form>



</body>
</html>