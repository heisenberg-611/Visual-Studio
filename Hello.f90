program a2q4
    implicit none
    integer ::h,maxv ,minv,n

     real::e,x,f,p,q,posip,posiq
     maxv=0
     n=0

p=1.61
q=0
    do x= 0,2,.01
    f =5*(sin(x**2))+ log (x+2)-(x**3)
    print *,f


         if (f>p) then
            p=f
            n=n+1
            end if
            end do
             write(*,*)" max", p,n
    do x= 0,2,.01
    f =5*(sin(x**2))+ log (x+2)-(x**3)

             if ( f<q) then
                q=f
            n=n+1


        end if
    end do


    print *," min =",q,n



end program