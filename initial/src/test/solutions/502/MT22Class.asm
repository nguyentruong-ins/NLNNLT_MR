.text
.globl main
main:
	li $8,50
	li $9,11
	add $16,$8,$9

	# Call putInt Function
	add $4,$16,$zero
	li $2,1
	syscall

	li $2,10
	syscall
