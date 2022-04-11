class Solution:
	def subdomainVisits(self, cpdomains):
		count = {}      # this dictionary will store subdomains with the number of visits
		for domain in cpdomains:        # let's split subdomains and visits
			item = domain.split(' ')        # separate visits from a domain
			visits = int(item[0])       # first item is a number of visits
			whole_domain = item[1]       # and the second item is a whole domain
			whole_domain = whole_domain.split('.')      # to iterate let's split it when commas
			subdomains = ['.'.join(whole_domain[i:]) for i in range(len(whole_domain))]
			# when we've got all subdomains, it's enough to add visits to the count dictionary
			for subdomain in subdomains:
				if subdomain not in count:      # if there isn't any occurance, just treat as zero - you could use default dictionary as well
					count[subdomain] = 0

				count[subdomain] += visits      # add the number of visits

		return [f"{value} {key}" for key, value in count.items()]
