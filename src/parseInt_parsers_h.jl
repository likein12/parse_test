using Parsers

function parseInt_parsers(num_str::AbstractString)
	return Parsers.parse(Int,num_str)
end

@time a = map(parseInt_parsers,split(readline()))
