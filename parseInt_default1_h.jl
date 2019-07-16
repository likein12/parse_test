function parseInt_default1(num_str::AbstractString)
	return parse(Int,num_str)
end

@time a = map(parseInt_default1,split(readline()))
