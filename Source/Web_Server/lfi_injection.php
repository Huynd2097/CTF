<?php


if (isset($_GET['type']) && isset($_GET['file'])) {
    $file = $_GET['file'];
    switch ($_GET['type']) {
        case '':
        case 'raw':
            include( raw($file) );
            break;
        case 'replace':
            include( replace($file) );
            break;
        case 'encode':
            include( encode($file) );
            break;
        case 'addExt':
            include( addExt($file) );
            break;

    }
    
} else {
    echo '
    try to read ../flag.txt<br><br>

    <li><a href="?type=raw&file=login.php">raw</a></li> <br>
    <li><a href="?type=replace&file=login.php">replace</a></li> <br>
    <li><a href="?type=encode&file=login.php">encode</a></li> <br>
    <li><a href="?type=addExt&file=login">addExt</a></li> <br>

    <p> <b>Hint: </b> <i>"?...=php://filter/convert.base64-encode/resource=...</i>"
    ';
}

function raw($file)
{
    return $file;
}

function replace($file)
{
    return str_replace('../', '', $file);
}   

function encode($file)
{
    return urlencode($file);
}

function addExt($file)
{
    return $file . '.php';
}
?>

