Algorithm:
Algorithm place (k, i)
//return true if a queen can be placed in k th row and ith column, Otherwise false.
//X[ ] is a global array whose first k-1 values have been set.
// Abs function returns the absolute value of r.
{


For j=1 to k-1 do
//checking for attacking position in same column, same row, or in diagonal

if ((X[j] ==i ) or X[j] == k Or (abs (X [j]-i)==abs (j-k)))
	Then return false;
else
	Return true;
}


Algorithm Nqueen (k, n)
//using backtracking it prints all possible positions of n queens in ‘n*n’ chessboard. So that they are non-tracking.
{
For i=1 to n do
{
	If place (k,i) then
	{ 
		X[k]=i;
		If (k==n) then
			write (X[1:n]);
		Else
			Nqueen(k+1,n) ;
	} 
} 
}
