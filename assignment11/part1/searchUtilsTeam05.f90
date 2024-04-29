MODULE searchutils
    IMPLICIT NONE
  
  CONTAINS
  
    FUNCTION linearSearch(arr, x) RESULT(idx)
      REAL(8), DIMENSION(:), INTENT(IN) :: arr  ! Array to search
      REAL(8), INTENT(IN) :: x                  ! Value to search for in array
      INTEGER :: idx                           ! Result of the search. ie: "arr(idx) == x"
      INTEGER :: n                             ! Number of elements in the array
      INTEGER :: i
  
      n = SIZE(arr)  ! Determine size within Fortran
      idx = -1       ! Initialize idx to its default value
      
      DO i = 1, n
        IF (arr(i) == x) THEN
          idx = i
          EXIT  ! Exit the loop once x is found
        END IF
      END DO
    END FUNCTION linearSearch
  
    FUNCTION binarySearch(arr, x) RESULT(idx)
      REAL(8), DIMENSION(:), INTENT(IN) :: arr
      REAL(8), INTENT(IN) :: x
      INTEGER :: idx, lower, upper, mid
      INTEGER :: n
  
      n = SIZE(arr)
      idx = -1
      lower = 1
      upper = n
      
      DO WHILE (idx == -1 .AND. lower <= upper)
        mid = (lower + upper) / 2
        IF (arr(mid) == x) THEN
          idx = mid
        ELSE IF (arr(mid) < x) THEN
          lower = mid + 1
        ELSE
          upper = mid - 1
        END IF
      END DO
    END FUNCTION binarySearch
    
  END MODULE searchutils
  