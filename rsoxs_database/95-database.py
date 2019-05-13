print(f'Loading {__file__}...')


def new_user():
    print("This information will tag future data until this changes, please be as thorough as possible/n"
          "current values in parentheses, leave blank for no change")
    #archive the current user information


    user = input('Your username (directory name) ({}): '.format(RE.md['user']))
    if user is not '':
        RE.md['user'] = user
    # search through user database for existing user, give option to load that users's information if it exists
    # if so, load that user info into RE.md, so those values will default the following choices
    # get list of possible users from pass? - avoiding duplication is key
    # if new, clear out RW.md, so suggestions don't inadvertently duplicate last user's info

    proposal_id = input('Your proposal id ({}): '.format(RE.md['proposal_id']))
    # give choices if user has past options - get from pass if possible
    if proposal_id is not '':
        RE.md['proposal_id'] = proposal_id
        # add proposal id to the user's list of proposal ids

    institution = input('Your institution ({}): '.format(RE.md['institution'])) #give choices if there are multiple
    if institution is not '':
        RE.md['institution'] = institution
        # add instiution to the list of user instituions (if it isn't already there)

    email = input('Your email address ({}): '.format(RE.md['email'])) #give choices if there are multiple
    if email is not '':
        RE.md['email'] = email
        # add email to the user record (if it isn't already there) or overwrite
        # search through other users and if duplicate, ask if they want to use that existing user

    phone = input('Your phone ({}): '.format(RE.md['phone'])) #give choices if there are multiple
    if phone is not '':
        RE.md['phone'] = phone
        # add phone to the user record (if it isn't already there) or overwrite
        # search through other users and if duplicate, ask if they want to use that existing user

    project = input('Your project ({}): '.format(RE.md['project']))
    # search through samples related to user, give options
    if project is not '':
        RE.md['project'] = project
        # add project to user list of pojects

    notes = input('Any special notes to add to metadata? ({}): '.format(RE.md['notes']))
    if notes is not '':
        RE.md['notes'] = notes
        # overwrite notes in user record

    #only if there is a new user
    user_first_name = input('Your first name ({}): '.format(RE.md['user_first_name']))
    if user_first_name is not '':
        RE.md['user_first_name'] = user_first_name
    user_last_name = input('Your last name ({}): '.format(RE.md['user_last_name']))
    if user_last_name is not '':
        RE.md['user_last_name'] = user_last_name
        # search through other users and if duplicate, ask if they want to use that existing user (show all info)

    # load or create new user id from database
    # RE.md['userid'] = userid
    test = input('Add new sample?')
    if test.startswith(('y','Y')) or test=='':
        new_sample()


def new_sample():
    print("This information will tag future data until this changes, please be as thorough as possible/n"
          "current values in parentheses, leave blank for no change")
    # archive the current user information

    sample_name = input('Your sample name (added to filename - be concise) ({}): '.format(RE.md['sample_name']))
    if sample_name is not '':
        RE.md['sample_name'] = sample_name
    # search through sample database for existing user, give option to load previous sample information if it exists

    # if a old sample was found:
    # isnew = input('Sample with this name was previously loaded {} Is this sample new? '.format(previousdate))

    # if new, clear out RW.md, so suggestions don't inadvertently duplicate last sample's info
    # if not new, load that sample info into RE.md, so those values will default the following choices

    sample_desc = input('Describe this sample ({}): '.format(RE.md['sample_desc']))
    # give choices if user has past options - get from pass if possible
    if sample_desc is not '':
        RE.md['sample_desc'] = sample_desc
        #overwrite the sample_desc in the database

    project_name = input('Project ({}): '.format(RE.md['project_name']))  # give current past projects as options
    if project_name is not '':
        RE.md['project_name'] = project_name

    sample_institution_id = input('Institution ({}): '.format(RE.md['sample_institution_id']))
    # give user institution as choice as well (if different than existing sample info)
    if sample_institution_id is not '':
        RE.md['sample_institution_id'] = sample_institution_id
        # this must be a multiple choice

    composition = input('Sample composition (this will help with analysis)\n'
                        'use a chemical formula if possible ({}): '.format(RE.md['composition']))
    if composition is not '':
        RE.md['composition'] = composition

    density = input('Sample density (this will help with analysis)({}): '.format(RE.md['density']))
    if density is not '':
        RE.md['density'] = density

    thickness = input('Sample thickness (this will help with analysis) ({}): '.format(RE.md['thickness']))
    if thickness is not '':
        RE.md['thickness'] = thickness

    sample_notes = input('Any notes to add to metadata ({}): '.format(RE.md['sample_notes']))
    if sample_notes is not '':
        RE.md['sample_notes'] = sample_notes

    state = input('Choose sample state ({}): '.format(RE.md['state']))
    if state is not '':
        RE.md['state'] = state
        # overwrite state in user record

    # load or create new sample id from database
    # RE.md['sample_id'] = sample_id

    # need a bar_id and slot_id
    # test = input('Add to a slot on a bar?') # add the current selected bar_id, slot_name to this sample,
    #                               or leave blank and suggest creating a new bar
    # ask if add to current slot?


def new_bar():
    holder_name = input('Name for this holder: ') # look up this name,
    # make sure nothing of this name for this user has been loaded before
    # if so, ass if they want to open up existing bar instead (exit if this is the case, the rest is only for new bars)
    user_id = input('Primary user for this bar: ') # add current user as default, otherwise search for users somehow
    # return the database user_id number
    institution_id = input('Primary institution for this bar: ') # add curren instiution by default, drop down list
    proposal_id = input('primary proposal id to associate with this bar: ') # curent proposal ID as default (get from pass?)
    # add current date to the date loaded list
    notes = input('notes for this bar: ')
    slots = []
    slotname = input('move to position, then enter slot name here (blank to end): ')
    while slotname is not "":
        newslot = new_slot_here(slotname)
        slots.append(newslot)
        print('added slot')# pretty print slot info
        slotname = input('move, then add another slot name for this location (blank to end): ')
    print('added {} slots'.format(len(slots)))

def new_slot_nere(slot_name):
    return name
    # use the current sample position and bar, and add a slot entry to the bar with that location and the input name

