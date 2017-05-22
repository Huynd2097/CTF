 
<form action="" method="post">
  	FirstName&nbsp;<br/>
  	<input id="user" type="text" name="firstname" /><br/><br/>
	LastName&nbsp;<br/>
	<input id="pass" type="text" name="lastname" /><br/><br/>
	<input type="submit" value="Register/Find" /><br/><br/>
	<br/><br/>
</form>


<p class='return_value'></p>



 <?php
$servername = "localhost";
$username = "root";
$password = "password";
$dbname = "myDB";

// Create connection
$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// $id = '';

// $sql = "SELECT id, firstname, lastname FROM myTable
// WHERE id='$id'";
// $result = mysqli_query($conn, $sql);

// if (mysqli_num_rows($result) > 0) {
//     // output data of each row
//     while($row = mysqli_fetch_assoc($result)) {
//         echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
//     }
// } else {
//     echo "0 results";
// }




if ( isset($_POST["firstname"]) && isset($_POST["lastname"]) ){
	$firstname = $_POST["firstname"];	
	$lastname = $_POST["lastname"];

	if ($_POST["lastname"]){
		$sql = "INSERT INTO myTable (firstname, lastname, email, reg_date)
		VALUE ('$firstname', '$lastname', '$firstname'"."'@gmail.com', NOW())";

		if ($conn->query($sql) === TRUE) {
		    echo "New record created successfully";
		} else {
		    echo "Error: " . $sql . "<br>" . $conn->error;
		}

	} elseif ($_POST["firstname"]) {

		$sql = "SELECT id, firstname, lastname, email, reg_date FROM myTable
				WHERE firstname='$firstname'";

		$result = mysqli_query($conn, $sql);
		if (mysqli_num_rows($result) > 0) {
		    // output data of each row
		    while($row = mysqli_fetch_assoc($result)) {
	        echo "id: " . $row["id"]. " - Name: " . $row["firstname"]. " " . $row["lastname"]. "<br>";
		  	}
		} else {
		    echo "Not found!";
		}
	}


}

$conn->close();
?>
