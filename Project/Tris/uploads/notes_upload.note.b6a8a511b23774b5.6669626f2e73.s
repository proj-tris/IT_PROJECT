	.file	"array.c"
	.global	array
	.data
	.align	2
	.type	array, %object
	.size	array, 40
	.global	main
	.type	main, %function
main:
	
	@recursively computes the value of nth fibonacci number
	adr       r0, .LC3                    
	bl        putstring  

	mov r2, #1
	
	
	bl myScan				@Scan Number 
	mov r0,r1				@Mov Value of n into r0

	bl fact					@compute factorial
	mov r1,r3				@r3 has the value of nth fibo number
	bl myPrint				@print result
	bl exit
	

	@end you code here

fact:
	stmdb sp!, {r1,r2,lr}
	
	cmp r0, #1 				@ if r0==1 r3=1
	moveq r3,#1
	ldmeqia sp!, {r1,r2,pc}
	
	cmp r0, #2				@ if r0==1 r3=2
	moveq r3, #1
	ldmeqia sp!, {r1,r2,pc}

	mov r2, r0				@ store n in r2
	sub r0, r0, #1
	
	bl fact
	mov r1, r3				@ r3 now contains the value of the n-1 fibo term. store it in r1
	
	sub r0, r2, #2				@ n=n-1
	bl fact
						@ r3 now contains the value of the n-2 fibo term
	add r3, r3, r1				@ fibo(n) =fibo(n-1)+fibo(n-2)

	
	mov r1, r3
	ldmia sp!, {r1,r2, pc}
	
.global putstring
putstring:                                 @print string 
	    stmfd     r13!, {r4-r12, lr}
	    mov       r1, r0
	    mov       r0, #4
	    swi       0x123456
	    ldmfd     r13!, {r4-r12, pc}
.global	myPrint
myPrint:                                    @print integer value of r1
	@prints an integer present in r1
	stmfd	sp!,{r0,r1,r2,r3,r7, lr}
	add	r7, sp, #0
	adr 	r0, .LC0
	bl	printf
	mov	r0, #0
	ldmfd	sp!,{r0,r1,r2,r3,r7, pc}


.global myScan
myScan:			@scan integer or character  in r1
	@scans an integer and returns it in r1
	stmfd   sp!, {r0,r2,r3,r7, lr}
	sub 	sp, sp, #8
	add     r7, sp, #0
	adr     r0, .LC1
	add	r1, sp, #4
	bl      scanf
	ldr	r1, [sp, #4]
	mov     r0, #0
	add	sp, sp, #8
	ldmfd	sp!,{r0,r2,r3,r7, pc}


.LC0:                 @print int
	.ascii	"Result = %d\012\000"
	.align 2
.LC1: 			@scan int
	.ascii "%d\000"
	.align 2
.LC2:
	.ascii	"%c\012\000"   @print char
	.align 2
.LC3:
	.ascii "Give Number \000" @print string


