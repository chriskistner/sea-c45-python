# Name: ...
# CSE 140
# Homework 2: DNA analysis

# This program reads DNA sequencer output and computes statistics, such as
# the GC content.  Run it from the command line like this:
#   python dna_analysis.py myfile.fastq


###########################################################################
### Libraries
###

# The sys module supports reading files, command-line arguments, etc.
import sys


###########################################################################
### Read the nucleotides into a variable named seq
###

# You need to specify a file name
if len(sys.argv) < 2:
    print("You must supply a file name as an argument when running this program.")
    sys.exit(2)
# The file name specified on the command line, as a string.
filename = sys.argv[1]
# A file object from which data can be read.
inputfile = open(filename)

# All the nucleotides in the input file that have been read so far.
seq = ""
# The current line number (= the number of lines read so far).
linenum = 0


for line in inputfile:
    linenum = linenum + 1
    # if we are on the 2nd, 6th, 10th line...
    if linenum % 4 == 2:
        # Remove the newline characters from the end of the line
        line = line.rstrip()
        seq = seq + line


###########################################################################
### Compute statistics
###

# Total nucleotides seen so far.
total_count = 0
# Number of G and C nucleotides seen so far.
gc_count = 0

at_count = 0
a_tally = 0
g_tally = 0
c_tally = 0
t_tally = 0
total_n = 0
total_l = len(seq)

# for each base pair in the string,
for bp in seq:
    # increment the total number of bps we've seen
    total_count = total_count + 1

    # next, if the bp is a G or a C,
    if bp == 'C' or bp == 'G':
        # increment the count of gc
        gc_count = gc_count + 1

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count

# Print the answer
print('GC-content:', gc_content)
    elif bp == 'A' or bp == 'T':
            at_count = at_count + 1

# Increments the total number of A, G, C, and T values in the entire sequence
for bp in seq:
    if bp == 'A':
        a_tally = a_tally + 1
    elif bp == 'G':
        g_tally = g_tally + 1
    elif bp == 'C':
        c_tally = c_tally + 1
    elif bp == 'T':
        t_tally = t_tally + 1

# Returns the total numbber of nucleotides in the sequence.
for bp in seq:
    total_n = a_tally + t_tally + c_tally + g_tally

ratio = (a_tally + t_tally) / (g_tally + c_tally)

# divide the gc_count by the total_count
gc_content = float(gc_count) / total_count
at_content = float(at_count) / total_count

# Checks the percentage of GC in SEQ and rpeorts back a level  message
gc_level = ""
if gc_content > 0.6:
    gc_level = "High GC Content"
elif gc_content < 0.4:
    gc_level = "Low GC Content"
else:
    gc_level = "Moderate GC Content"

# Print the answer
print(inputfile)
print('GC-content:', gc_content)
print('AT-content:', at_content)
print('AT/GC Ratio:', ratio)
print(gc_level)
print('Nucleotides in sequence:', total_n)
print('Total nucleotides are:', a_tally, 'As', c_tally, 'Cs', g_tally, 'Gs', \
t_tally, 'Ts')
print('Length of Sequence:', total_l)
