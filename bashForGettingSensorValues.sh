for i in {0..99}; 
do 
	regval=$(i2cget -y 1 0x1c 0x$i); 
	echo "Address 0x$i has value: $regval"; 
done

