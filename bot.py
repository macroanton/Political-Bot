import praw
import random
import datetime
import time

madlibs1=["[Hyper capitalist are] more than 1000 times richer than the [entry for] the 1%.  And [Hyper-capitalist are] [over] 2 million times [wealthier] than the average american."
    ]
    
madlibs2= [
    "[My dog] should be the national mascot." "[My doggy] has more to provide the american people than [the leading competitor] ever has" "There shouldn't be a law that doesn't allow [people] to [eat cabbage]"
]

madlibs3=[
    "My political [opponent] is [working] with [my AA sponser], [Guy Fierri] and [the prince of Narnia]"
]

madlibs4=["I, [Mike Izbicki], want [an America] where greedy [insurance companies] and [internet photographers] cannot make a mockery of [my poetry]."]

madlibs5=['[When] I’m elected, I’ll make sure [greedy doctors] and [military-industrial warmongers] can’t [sabotage] our right to [transparency].']
madlibs6=['Ask not what your [country] can do for [you,] ask what [you] can do for your [country.] -[John F. Kennedy] 1961']

total_madlibs=[madlibs1,madlibs2, madlibs3, madlibs4, madlibs5, madlibs6]

replacements = {
    'Hyper capitalist are' : ['Elon Musk is', 'Jeff Bezos', 'Larry Ellison is', 'Larry Page is', 'Mark Zuckerberg is'],
    'Hyper-capitalist are' : ['Elon Musk is', 'Jeff Bezos', 'Larry Ellison is', 'Larry Page is', 'Mark Zuckerberg is'],
    'entry for' : ['entrance to', 'requirments to be considered in', 'range for',],
    'over' : ['more than', 'greater than'],
    'wealthier' : ['richer', 'the amount of cash-money', 'the amount of clout'],
    'My dog'  : ['Clifford', 'Marley', 'Scooby-doo', 'Air-bud'],
    'My doggy'  : ['Clifford', 'Marley', 'Scooby-doo', 'Air-bud'],
    'the leading competitor' : ['Bugs-Bunny', 'a half-chewed piece of gum', 'Sea-biscuit'],
    'people' : ['henry from band camp', 'the 4th Jonas brother', 'Professor Izbicki'],
    'eat cabbage' : ['project cartoons on the moon', 'give a heated debate on the efficacy of laxatives', 'eat cow eyeballs', 'drop it like its hot'],
    'opponent' : ['arch-enemy', 'great-uncle Gary', 'long-lost twin cousin'],
    'working' : ['collaborating', 'conspiring', 'having brunch'],
    'my AA sponser' : ['Fonzie', 'Homer Simpson', 'Michael Scott', 'Walter White'],
    'Guy Fierri' : ['Tony Soprano', 'Jesse Pinkman', 'Ron Swanson'],
    'the prince of Narnia' : ['Brandon from tutoring', 'Joey from tutoring', 'Ton from Tutoring'],
    'Mike Izbicki' : ['the prettiest princess', 'the rightful king of Texas', 'the creator of the snacks that smile back'],
    'an America' : ['a world'],
    'insurance companies' : ['estranged land-lords', 'guys at the bust stop', 'parole officers'],
    'internet photographers' : ['the 7 dwarfs', 'the ladybug from A Bugs Life', 'Shaggy'],
    'my poetry' : ['my index finger', 'the great state of Michigan', 'the metaphysical properties of eating grass'],
    'When' : ['If'],
    'greedy doctors' : ['my index finger', 'the great state of Michigan', 'the metaphysical properties of eating grass'],
    'military-industrial warmongers' : ['henry from band camp', 'the 4th Jonas brother', 'Professor Izbicki'],
    'sabotage' : ['ruin', 'infringe upon'],
    'transparency' : ['wear white after labor day', 'eat jars of butter', 'manipulate the free world'],
    'country' : ['pyramid-scheme', 'cousin-gary', 'political-propaganda'],
    'country.' : ['pyramid-scheme.', 'cousin-gary.', 'political-propaganda.'],
    'you,' : ['the people who have never seen a jellyfish,', 'beastiality supporters,', 'President Chodosh,'],
    'you' : ['the people who have never seen a jellyfish', 'beastiality supporters', 'President Chodosh'],
    'John F. Kennedy' : ['the prettiest princess', 'the rightful king of Texas', 'the creator of the snacks that smile back'],

    }

def generate_comment():
    '''
    This function generates random comments according to the patterns specified in the `madlibs` variable.
    To implement this function, you should:
    1. Randomly select a string from the madlibs list.
    2. For each word contained in square brackets `[]`:
        Replace that word with a randomly selected word from the corresponding entry in the `replacements` dictionary.
    3. Return the resulting string.
    For example, if we randomly seleected the madlib "I [LOVE] [PYTHON]",
    then the function might return "I like Python" or "I adore Programming".
    Notice that the word "Programming" is incorrectly capitalized in the second sentence.
    You do not have to worry about making the output grammatically correct inside this function.
    '''

    s= (random.choice(total_madlibs))
    s = random.choice(s)
    for k in replacements.keys():
        s=s.replace('['+k+']', random.choice(replacements[k]))  
    return s

reddit = praw.Reddit('bot')

# select a "home" submission
submission_url= 'https://www.reddit.com/r/BotTown2/comments/r0yi9l/main_discussion_thread/'
submission = reddit.submission(url=submission_url)
 
# while you are writing and debugging your code, 
# you probably don't want it to run in an infinite loop;
# you can change this while loop to an if statement to make the code run only once
while True:
    print()
    print('new iteration at:',datetime.datetime.now())
    print('submission.title=',submission.title)
    print('submission.url=',submission.url)

# gets a list of all of the comments in the submission
    all_comments = []
    submission.comments.replace_more(limit=None)
    all_comments = submission.comments.list()
    print('len(all_comments=)', len(all_comments))

# filters all_comments to remove comments that were generated by your bot
    replied_to = []
    not_my_comments = []
    for comment in all_comments:
        if comment.author != 'Bottle__' and comment.author != None:
            not_my_comments.append(comment)
    print('len(not_my_comments)=',len(not_my_comments))

# posts top level comment in the thread, if not already present 
    has_not_commented = len(not_my_comments) == len(all_comments)
    print('has_not_commented=', has_not_commented)
    if has_not_commented:
        text = generate_comment()
        submission.reply(text)   
    
# filters the not_my_comments list to also remove comments that 
# you've already replied to
    comments_without_replies = []    
    for comments in not_my_comments:
        havent_replied = True
        for replies in comments.replies:
            try:
                if replies.author == 'BurberryBot':
                    havent_replied  = False
                    break
            except IndexError:
                pass
            if havent_replied:
                comments_without_replies.append(replies)
    print('comments without replies=',len(comments_without_replies))

# randomly selects a comment from the comments_without_replies list,
# and replies to that comment
    comment = random.choice(comments_without_replies)
    try:
        comment.reply(generate_comment())
    except praw.exceptions.APIException :
        print('not replying to a comment that has been deleted')

# selects a new submission for the next iteration from 5 hottest submissions
    submission = random.choice(list(reddit.subreddit("BotTown2").hot(limit=5)))
    time.sleep(40) 