import math

def binomial_probability(n, k):
    # Calculate the binomial coefficient
    binomial_coefficient = math.comb(n, k)
    return binomial_coefficient 

''' Question:It is known that 10% of article manufactured are defective. 
What is the probability that in a random sample space 12 such articles,9 are defective?'''

''' The repeated selection of article in a random sample space are bernauli trails.
Let X denote the number of times of selective defective article in arandom sample space of 12 articles.'''

#here
p=0.1 # Probability of an article being defective
q=0.9
n=12  # Total sample size
k=9
'''The binomial distribution of x is given by,
 
                                           p(x=r)=(nCr)(p^r)(q^(n-r))'''

'''To calculate probability of exavtly 9 defective article in sample of 12 is:
                        
                                            p(x=9)=(12C9)(0.1^9)(0.9)^3'''



    
# Calculate the probability
probability = binomial_probability(n,k) * (p ** k) * ((q) ** (n-k))
    
    



# Print the result
print("The probability that exactly 9 out of 12 randomly sampled articles are defective is:", "{:.8f}".format(probability))
