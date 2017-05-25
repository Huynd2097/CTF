var _global = 0


var ð= "\x71\x11\x24\x59\x8d\x6d\x71\x11\x35\x16\x8c\x6d\x71\x0d\x39\x47\x1f\x36\xf1\x2f\x39\x36\x8e\x3c\x4b\x39\x35\x12\x87\x7c\xa3\x10\x74\x58\x16\xc7\x71\x56\x68\x51\x2c\x8c\x73\x45\x32\x5b\x8c\x2a\xf1\x2f\x3f\x57\x6e\x04\x3d\x16\x75\x67\x16\x4f\x6d\x1c\x6e\x40\x01\x36\x93\x59\x33\x56\x04\x3e\x7b\x3a\x70\x50\x16\x04\x3d\x18\x73\x37\xac\x24\xe1\x56\x62\x5b\x8c\x2a\xf1\x45\x7f\x86\x07\x3e\x63\x47";function exp(x,y){
return x^y;
}
function exp2sub1(y){
var z = 0;
	for(var i=0;
i<y;
i++){
z += Math.pow(2,i);
}
	return z;

}

function ___(y){
	var z = 0;
	for(var i=8-y;	i<8;i++){
	z += Math.pow(2,i);
	}
	return z
}

 function ____(x,y){
	y = y % 8;
	Ï = exp2sub1(y);Ï = (x & Ï) << (8-y);return (Ï) + (x >> y);
}

function _____(x,y){
	y = y % 8;
	Ï = ___(y);Ï = (x & Ï) >> (8-y);return ((Ï) + (x << y)) & 0x00ff;
}

function ______(x,y){
return	_____(x,y)
}

function encrypt(data,key){
	data1 = "";________2 = "";
	for(var i=0;i<data.length;	i++){		
		c = data.charCodeAt(i);
		if(i != 0){
			t = data1.charCodeAt(i-1)%2;
			switch(t)
			{
				case 0:cr = exp(c, key.charCodeAt(i % key.length));break;
				case 1:cr = ______(c, key.charCodeAt(i % key.length));break;
			}

		}
		else{
			cr = exp(c, key.charCodeAt(i % key.length));
		}
		data1 += String.fromCharCode(cr);
	}
	return data1;
}

function __________(þ){
var ŋ=0;
for(var i=0;i<þ.length;i++){
ŋ+=þ["charCodeAt"](i)
}

if(ŋ==8932){
	console.log(_global);
// var ç=window.open("","","\x77\x69\x64\x74\x68\x3d\x33\x30\x30\x2c\x68\x65\x69\x67\x68\x74\x3d\x32\x20\x30");ç.document.write(þ)
}
else{
// console.log(ŋ);
}

}

var alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZqwertyuiopasdfghjklzxcvbnm".split("");

for (var i = 0;  i <52; i++)
for (var j = 0;  j<52; j++)
for (var k = 0; k <52; k++)
for (var l = 0; l <52; l++){
	console.log(alphabet[i]+alphabet[j]+alphabet[k]+alphabet[l]);
}




for(_global=0; _global < 10000; ++_global)
{
__________(encrypt(ð,_global.toString()));
}

@(kÚED/È_â4 >¼èzH¶E:"E°"õâocXµ7db¸À]Ü=ÓXD^"}Ú%ær09efo@JA,=Ó`BÐo&iTÅþ¿pR~
@$²¼XD #Ú@8v.>Ñxz#t!èmÂö@c ¢ntkTÀ f_'êR#\)Í0rhcöa,1§0BHÐcLj½E>tN³àÆr
B&+lZH$!­r,ãåÉZ'