% rebase('layout.tpl', title='Employee Information for Department')

<h2> Department: {{department}} </h2><br>

<p>
<table class='table'>
<tr><th> EID </th><th> Name </th><th> Wage </th><th> Hrs </th><th> Pay </th></tr>
% for row in rows:
	<tr align = 'left'>
	% for col in row:
		<td>{{col}}</td>
	%end
	</tr>
%end
</table>
</p>