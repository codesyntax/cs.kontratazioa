The Aldaketa content type
===============================

In this section we are tesing the Aldaketa content type by performing
basic operations like adding, updadating and deleting Aldaketa content
items.

Adding a new Aldaketa content item
--------------------------------

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

Then we select the type of item we want to add. In this case we select
'Aldaketa' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Aldaketa').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Aldaketa' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Aldaketa Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

And we are done! We added a new 'Aldaketa' content item to the portal.

Updating an existing Aldaketa content item
---------------------------------------

Let's click on the 'edit' tab and update the object attribute values.

    >>> browser.getLink('Edit').click()
    >>> browser.getControl(name='title').value = 'New Aldaketa Sample'
    >>> browser.getControl('Save').click()

We check that the changes were applied.

    >>> 'Changes saved' in browser.contents
    True
    >>> 'New Aldaketa Sample' in browser.contents
    True

Removing a/an Aldaketa content item
--------------------------------

If we go to the home page, we can see a tab with the 'New Aldaketa
Sample' title in the global navigation tabs.

    >>> browser.open(portal_url)
    >>> 'New Aldaketa Sample' in browser.contents
    True

Now we are going to delete the 'New Aldaketa Sample' object. First we
go to the contents tab and select the 'New Aldaketa Sample' for
deletion.

    >>> browser.getLink('Contents').click()
    >>> browser.getControl('New Aldaketa Sample').click()

We click on the 'Delete' button.

    >>> browser.getControl('Delete').click()
    >>> 'Item(s) deleted' in browser.contents
    True

So, if we go back to the home page, there is no longer a 'New Aldaketa
Sample' tab.

    >>> browser.open(portal_url)
    >>> 'New Aldaketa Sample' in browser.contents
    False

Adding a new Aldaketa content item as contributor
------------------------------------------------

Not only site managers are allowed to add Aldaketa content items, but
also site contributors.

Let's logout and then login as 'contributor', a portal member that has the
contributor role assigned.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = 'contributor'
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)

We use the 'Add new' menu to add a new content item.

    >>> browser.getLink('Add new').click()

We select 'Aldaketa' and click the 'Add' button to get to the add form.

    >>> browser.getControl('Aldaketa').click()
    >>> browser.getControl(name='form.button.Add').click()
    >>> 'Aldaketa' in browser.contents
    True

Now we fill the form and submit it.

    >>> browser.getControl(name='title').value = 'Aldaketa Sample'
    >>> browser.getControl('Save').click()
    >>> 'Changes saved' in browser.contents
    True

Done! We added a new Aldaketa content item logged in as contributor.

Finally, let's login back as manager.

    >>> browser.getLink('Log out').click()
    >>> browser.open(portal_url + '/login_form')
    >>> browser.getControl(name='__ac_name').value = portal_owner
    >>> browser.getControl(name='__ac_password').value = default_password
    >>> browser.getControl(name='submit').click()
    >>> browser.open(portal_url)


