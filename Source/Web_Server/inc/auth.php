
<?php
$USER='admin';
$PASSWORD="F098cdrrJFERrgseijIJ";
$FLAG='flag{secret_flag}';

$return['status'] = 'Authentication failed!';
//use jquery
if (isset($_POST["auth"]))  { 
    // retrieve JSON data
    $auth = @json_decode($_POST['auth'], true);
    // check login and password (sha256)
    if($auth['data']['username'] == $USER && !strcmp($auth['data']['password'], $PASSWORD)){
        $return['status'] = "Access granted! The validation password is: $FLAG";
    }
}
print json_encode($return);
?>

