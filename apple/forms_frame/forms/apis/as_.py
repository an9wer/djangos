from django import forms


class AsTableForm(forms.Form):
    table_field = forms.CharField()


class AsUlForm(forms.Form):
    ul_field = forms.CharField()


class AsPForm(forms.Form):
    p_field = forms.CharField()



"""
在 html 中：

    {{ form.as_table }} 每个 field 都会使用 <tr> 标签包裹，
    需要我们手动加上 <tabble> 标签包裹该 form，否则不会显示 table 的效果。

    {{ form.as_ul }} 每个 field 都会使用 <li> 标签包裹，
    需要我们手动加上 <ul> 标签包裹该 form，否则不会显示 ul 的效果。

    {{ form.as_p }} 每个 field 都会使用 <p> 标签包裹。

    单单使用 {{ form }} 与 {{ form.as_table }} 等价。


    >>> t = AsTableForm()
    >>> print(t)
    <tr><th><label for="id_table_field">Table field:</label></th><td> <input type="text" name="table_field" required id="id_table_field" /></td></tr>
    >>>
    >>> print(t.as_table())
    <tr><th><label for="id_table_field">Table field:</label></th><td> <input type="text" name="table_field" required id="id_table_field" /></td></tr>

    >>> u = AsUlForm()
    >>> print(u.as_ul())
    <li><label for="id_ul_field">Ul field:</label> <input type="text" name="ul_field" required id="id_ul_field" /></li>

    >>> p = AsPForm()
    >>> print(p.as_p())
    <p><label for="id_p_field">P field:</label> <input type="text" name="p_field" required id="id_p_field" /></p>

"""
