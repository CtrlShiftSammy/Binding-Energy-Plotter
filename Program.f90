program program
    implicit none
    real :: n, z, a, b, e, b_c
    integer :: i
    open(unit = 1 , file="data_cropped.txt")
    open(unit = 2 , file="data_cropped_with_formula.txt")
        do i = 1, 3558
            read (1, *) n, z, a, b, e
            b_c = (15.753 * a) - (17.804 * a ** (2.0 / 3.0))
            b_c = b_c - (0.7103 * (z ** 2) / a ** (1.0 / 3.0)) - (23.69 * ((n - z) ** 2 ) / a)
            b_c = b_c + 12.0 * ((-1) ** z + (-1) ** n) / (2.0 * a ** 0.5)
            b_c = b_c / a
            write (2, *) z, a, (b / 1000.0), b_c
        end do
    close(unit = 1)
    close(unit = 2)
end program