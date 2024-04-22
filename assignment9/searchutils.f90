!
!  Author:   Matthew Holland
!  Date:     2024/04/21
!
!  This file contains the search utilities required to do the functions of assignment9
!
!

MODULE searchutils
  IMPLICIT NONE

CONTAINS

  !  Declare linear search subroutine within the module
  FUNCTION linearSearch(arr, n, x) RESULT(idx)
    IMPLICIT NONE
    ! This function will perform a linear search on an array to find the value within the
    !   array. See: https://www.geeksforgeeks.org/linear-search/
    ! 
    REAL(8) :: arr(n)           ! Array to search
    INTEGER :: n                ! Number of elements in the array
    REAL(8) :: x                ! Value to search for in array
    INTEGER :: idx              ! Result of the search. ie: "arr(idx) == x"
    
    INTEGER :: i
    
    idx = -1  ! Initialize idx to its default value
    
    DO i = 1, n
      IF (arr(i) == x) THEN
        idx = i
      END IF
    END DO
  END FUNCTION linearSearch
  !  Declare binary search subrouting within the module
   
  FUNCTION binarySearch(arr, n, x) RESULT(idx)
    IMPLICIT NONE
    ! This function will perform a binary search on an array to find the value within the
    !  array. See: https://www.geeksforgeeks.org/binary-search/
    !  
    REAL(8) :: arr(n)       ! Array to search
    INTEGER :: n            ! Number of elements in the array
    REAL(8) :: x            ! Value to search for in array
    INTEGER :: idx          ! Result of the search. ie: "arr(idx) == x"
    
    INTEGER :: lower, upper, mid
    
    idx = -1            ! Initialize idx to its default value
    lower = 1           ! Initialize lower bound
    upper = n           ! Initialize upper bound
    
    DO WHILE (idx == -1 .AND. lower <= upper)
      mid = (lower + upper) / 2
      IF (arr(mid) == x) THEN
        idx = mid                ! If the value is found, that's it
      ELSE IF (arr(mid) < x) THEN
        lower = mid + 1          ! If the value is not found, but it's further in the array, then move the lower bound to keep traveling through the array.
      ELSE
        upper = mid - 1          ! If the value is not found, but it's back in the array, then move the lower bound to keep traveling through the array.
      END IF
    END DO
  END FUNCTION binarySearch
  
END MODULE searchutils
  
  
    


