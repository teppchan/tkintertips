#!/usr/bin/env ruby






while STDIN.gets
  if $_=~/\$import\((.+)\)/

    #print $_
    fname=$1
    open fname do |f|
      f.each do |l|
        print l
      end
    end
  else
    print $_
  end
end


