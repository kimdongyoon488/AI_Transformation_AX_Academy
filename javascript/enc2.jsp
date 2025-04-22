<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="EUC-KR"%>
<%
    request.setCharacterEncoding("UTF-8");
    String name = request.getParameter("name");
%>
<%="안녕하세요 " + name %>
