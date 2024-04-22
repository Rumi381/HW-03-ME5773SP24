!
!  Authors:   Md Jalal Uddin Rumi and Matthew Holland
!  Date:     2024/04/22
!
!  This file contains the main program to implement the functions for different scenarios
!
!

PROGRAM main_program
  USE searchutils
  IMPLICIT NONE

  INTEGER, PARAMETER :: N2 = 10000000
  REAL(8), dimension(10) :: arr_test=[1.d0,2.d0,4.d0,5.d0,6.d0,7.d0,9.d0,10.d0,11.d0,15.d0]
  REAL(8) :: arr2(N2)
  REAL(8) :: x, t_start, t_end, elapsed_time_linear, elapsed_time_binary
  INTEGER :: idx, n
  
  ! n = size(arr_test,1) ! Number of elements in the array.
  ! x = 7.d0        ! Search for value 7.0 in the array.
  
  ! Linear search on small array
  ! idx = linearSearch(arr_test,n,x)
  ! print*, "Index computed with linear search: ", idx

  ! Binary search on small array
  ! idx = binarySearch(arr_test,n,x)
  ! print*, "Index computed with binary search: ", idx

  ! Use here these two cases to evaluate performance.
  print*, " -------------------------- "
  print*, "Testing on a sorted array"
  print*, " -------------------------- "
  Call fillSortedArray(arr2)
  x = arr2(N2-1)   ! Value of interest: Second to last element.
  n = SIZE(arr2,1)

  ! Measure the CPU time of the linearSearch function.
  CALL CPU_TIME(t_start)
  idx = linearSearch(arr2,n,x)
  CALL CPU_TIME(t_end)
  elapsed_time_linear = t_end - t_start
  print*, "CPU Time for linear search: ", elapsed_time_linear
  print*, "Index computed with linear search: ", idx , N2-1
  print*, "was the value found?: ", arr2(idx)==x

  ! Measure the CPU time of the binarySearch function.
  CALL CPU_TIME(t_start)
  idx = binarySearch(arr2,n,x)
  CALL CPU_TIME(t_end)
  elapsed_time_binary = t_end - t_start
  print*, "CPU Time for binary search: ", elapsed_time_binary
  print*, "Index computed with binary search: ", idx, N2-1
  print*, "was the value found?: ", arr2(idx)==x
  print*, "Thus, binary search algorithm is ", elapsed_time_linear/elapsed_time_binary," times faster than linear search algorithm for a given sorted array."
  
  print*, " -------------------------- "
  print*, "Testing on an unsorted array"
  print*, " -------------------------- "
  Call fillUnsortedArray(arr2)

  x = arr2(N2/2-1) ! Value of interest: middle element -1.
  n = SIZE(arr2,1)

  ! Measure the CPU time of the linearSearch function on an unsorted array.
  CALL CPU_TIME(t_start)
  idx = linearSearch(arr2,n,x)
  CALL CPU_TIME(t_end)
  elapsed_time_linear = t_end - t_start
  print*, "CPU Time for linear search on unsorted array: ", elapsed_time_linear
  print*, "Index computed with linear search: ", idx
  print*, "was the value found?: ", arr2(idx)==x

  ! Measure the CPU time of the binarySearch function on an unsorted array.
  CALL CPU_TIME(t_start)
  idx = binarySearch(arr2,n,x)
  CALL CPU_TIME(t_end)
  elapsed_time_binary = t_end - t_start
  print*, "CPU Time for binary search on unsorted array: ", elapsed_time_binary
  print*, "Index computed with linear search: ", idx
  print*, "was the value found?: ", arr2(idx)==x
  print*, "Meaning the binary search algorithm is unable to find the x value in the given unsorted array. This is expected as the algorithm only works for a sorted array"

CONTAINS
  
  ! Fill an array with sorted values.
  SUBROUTINE fillSortedArray(array)
    
    IMPLICIT NONE
    REAL(8):: array(:)
    INTEGER :: i

    DO i=1,SIZE(array,1)
      array(i) = (i*3.d0)
    END DO

  END SUBROUTINE fillSortedArray

  ! Fill an array with unsorted values.
  SUBROUTINE fillUnsortedArray(array)
    
    IMPLICIT NONE
    REAL(8):: array(:)
    INTEGER :: i

    DO i=1,SIZE(array,1)
      array(i) = (-1.d0)**(i) * i*2.d0
    END DO

  END SUBROUTINE fillUnsortedArray

END PROGRAM main_program
