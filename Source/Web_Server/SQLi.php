<a href="?register"> Register </a> | <a href="?"> Login </a>
<br><br>
<p id="type"> <?php if (isset($_GET['register'])) echo "Register"; else echo "Login";?> </p>

<form action="" method="post">
  	Username&nbsp;<br/>
  	<input id="user" type="text" name="username" /><br/><br/>
	Password&nbsp;<br/>
	<input id="pass" type="password" name="password" /><br/><br/>
	<input type="submit" value="Submit" /><br/><br/>
	<br/><br/>
</form>


<p class='return_value'></p>



 <?php
$servername = "localhost";  
$username = "root";
$password = "password";
$dbName = "SQLi";
$tbName = "User";

// Create connection
$conn = new mysqli($servername, $username, $password);
// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// // Create database
// $sql = "CREATE DATABASE SQLi";
// if ($conn->query($sql) === TRUE) {
//     echo "Database created successfully";
// } else {
//     echo "Error creating database: " . $conn->error;
// }






// Create connection
$conn = new mysqli($servername, $username, $password, $dbName);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// // sql to create table
// $sql = "CREATE TABLE User (
// id INT(6) UNSIGNED AUTO_INCREMENT PRIMARY KEY,
// username VARCHAR(30) NOT NULL,
// password VARCHAR(30) NOT NULL,
// permission INT(2) DEFAULT 1 #
// )";

// if ($conn->query($sql) === TRUE) {
//     echo "Table MyGuests created successfully";
// } else {
//     echo "Error creating table: " . $conn->error;
// }



if ( isset($_POST["username"]) && isset($_POST["password"]) ){
	$username = $_POST["username"];	
	$password = $_POST["password"];
	if (!$username or !$password) {
		echo "Username or Password is empty!";
	} else {
		if (isset($_GET["register"])){
			$sql = "INSERT INTO User (username, password)
			VALUE ('$username', '$password')";

			if ($conn->query($sql) === TRUE) {
			    echo "Register successfully";
			} else {
			    echo $conn->error;
			}

		} else {

			$sql = "SELECT id, username, password FROM User
					WHERE username='$username' AND password='$password'";

			$result = mysqli_query($conn, $sql);
			if (mysqli_num_rows($result) > 0) {
			    // output data of each row
			    $row = mysqli_fetch_assoc($result);
		        echo " You are login! <br>"
		        		. "Username: " . $row["username"] ."<br>"
		        		. "Password: " . $row["password"]. "<br>";
			} else {
			    echo "Username or Password is wrong!";
			}
		}
	}

}

$conn->close();
?>
