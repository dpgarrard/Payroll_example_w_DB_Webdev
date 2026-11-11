% rebase('layout.tpl', title='Display Employees by Department')

<form action="/department" method="post">

<p><select name='department'> category
      <option value='shipping'>Shipping</option>
      <option value='maintenance'>Maintenance</option>
      <option value='environment'>Environment</option>
      <option value='advertising'>Advertising</option>

    </select>
</p>

<p><input type="submit"></p>

</form>