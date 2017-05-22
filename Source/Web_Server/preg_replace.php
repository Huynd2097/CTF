<legend>Regex evaluator</legend>
	<form METHOD="POST" action="">
	<div>
	<input type="text" name="search" placeholder="search" style="width:250px;">
	</div>
	<br />
	<div>
	<input type="text" name="replace" placeholder="replace" style="width:250px;">
	</div>
	<br />
	<div>
	<input type="text" name="content" placeholder="content" style="width:250px;">
	</div>
	<br />
	<button type="submit">Submit</button>
	</form>

<?php 


$dg='sf';

if (isset($_POST['search']) && isset($_POST['replace']) && isset($_POST['content'])) {
	$new = preg_replace($_POST['search'], $_POST['replace'], $_POST['content']);
	echo htmlentities($new);
} 



echo preg_replace('/(.*?)/e', 'file_get_contents("../flag.php")', 'aa');
?>