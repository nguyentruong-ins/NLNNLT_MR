.text
.globl main
main:
	li $8,100
	li $9,1000
	add $16,$8,$9

	# Call putInt Function
	add $4,$16,$zero
	li $2,1
	syscall

	li $2,10
	syscall
