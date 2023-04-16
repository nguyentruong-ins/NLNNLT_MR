.text
.globl main
main:
	li $8,1
	li $9,2
	sub $16,$8,$9

	# Call putInt Function
	add $4,$16,$zero
	li $2,1
	syscall

	li $2,10
	syscall
